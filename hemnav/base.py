# -*- coding: utf-8 -*-
"""Nav Base Module

Module Contains NAVWrapper which is the base class
for all classes related to Microsoft Navision Integration
"""
import datetime
import zeep

from .settings import Settings, RegionEnum
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
from enum import Enum


class NAVBase:
    """A simple NAV wrapper that creates a client based on region
    """

    def __init__(self, region, service_endpoint_name, code_unit=True):
        """Constructor method of nav base creates an instance of soap
        client(Zeep) based on endpoint name for Microsoft Navision.
        The client will be inherited and used by all subclasses of this class.

        Args:
            region (RegionEnum): What NAV configuration to use (eu or us)
            service_endpoint_name (str): NAV SOAP endpoint name.
            code_unit (bool, optional): There is 2 types of soap endpoints in
            Navision (Code Units and Pages).

        Raises:
            AttributeError: In case of wrong region
            Fault: Zeep faults in case of incorrect requests being made

        """

        self._service_name = service_endpoint_name
        self._region = region
        settings = Settings(region)
        session = Session()

        session.auth = HTTPBasicAuth(settings.nav_username, settings.nav_password)

        client_url = settings.base_url
        client_url += settings.store_name
        client_url += "/Codeunit" if code_unit else "/Page"
        client_url += "/{endpoint_name}".format(endpoint_name=service_endpoint_name)
        self._client = zeep.Client(client_url, transport=Transport(session=session))

    def _where(self, query: dict) -> list:
        """Method abstracts SOAP action (ReadMultiple) returns one or more
        result/s based of a filter(field,Criteria).

        Params:
            query [dict]: [{Field: Criteria}]
        Returns:
            list
        """

        filter_query = list(
            map(lambda key: {"Field": key, "Criteria": query[key]}, query.keys())
        )

        return self._client.service.ReadMultiple(filter=filter_query, setSize=0)

    def _create(self, fields: dict) -> dict:
        """Method abstracts SOAP action (Create) which is used to create entities
        in NAV

        Args:
            fields (dict): Attributes used to create an entity

        Returns:
            dict: Attributes of the created object
        """

        nav_object = {self._service_name: fields}
        return self._client.service.Create(**nav_object)

    def _get(self, fields: dict) -> dict:
        """Method abstracts SOAP action (Read) which is used to get an
        entity from NAV

        Args:
            fields (dict): Attributes used to get an entity

        Returns:
            dict: Attributes of the requested object
        """

        return self._client.service.Read(**fields)

    def _update_multiple(self, fields: dict) -> dict:
        """Method abstracts SOAP action (UpdateMultiple) which is used to Update an
        multiple entity objects in NAV

        Args:
            fields (dict): Attributes used to Update a list entity objects

        Returns:
            dict: Attributes of the Updated object
        """
        list_field = "_".join([self._service_name, "List"])
        nav_object = {list_field: {self._service_name: fields}}
        return self._client.service.UpdateMultiple(**nav_object)

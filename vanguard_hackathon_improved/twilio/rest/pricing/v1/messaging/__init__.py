# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page
from twilio.rest.pricing.v1.messaging.country import CountryList


class MessagingList(ListResource):
    """  """

    def __init__(self, version):
        """
        Initialize the MessagingList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.pricing.v1.messaging.MessagingList
        :rtype: twilio.rest.pricing.v1.messaging.MessagingList
        """
        super(MessagingList, self).__init__(version)

        # Path Solution
        self._solution = {}

        # Components
        self._countries = None

    @property
    def countries(self):
        """
        Access the countries

        :returns: twilio.rest.pricing.v1.messaging.country.CountryList
        :rtype: twilio.rest.pricing.v1.messaging.country.CountryList
        """
        if self._countries is None:
            self._countries = CountryList(self._version)
        return self._countries

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.MessagingList>'


class MessagingPage(Page):
    """  """

    def __init__(self, version, response, solution):
        """
        Initialize the MessagingPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.pricing.v1.messaging.MessagingPage
        :rtype: twilio.rest.pricing.v1.messaging.MessagingPage
        """
        super(MessagingPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of MessagingInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.pricing.v1.messaging.MessagingInstance
        :rtype: twilio.rest.pricing.v1.messaging.MessagingInstance
        """
        return MessagingInstance(self._version, payload)

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.MessagingPage>'


class MessagingInstance(InstanceResource):
    """  """

    def __init__(self, version, payload):
        """
        Initialize the MessagingInstance

        :returns: twilio.rest.pricing.v1.messaging.MessagingInstance
        :rtype: twilio.rest.pricing.v1.messaging.MessagingInstance
        """
        super(MessagingInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {'name': payload['name'], 'url': payload['url'], 'links': payload['links']}

        # Context
        self._context = None
        self._solution = {}

    @property
    def name(self):
        """
        :returns: The name
        :rtype: unicode
        """
        return self._properties['name']

    @property
    def url(self):
        """
        :returns: The url
        :rtype: unicode
        """
        return self._properties['url']

    @property
    def links(self):
        """
        :returns: The links
        :rtype: unicode
        """
        return self._properties['links']

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Pricing.V1.MessagingInstance>'

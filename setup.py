# coding: utf-8

"""
    cpaas api

    # Overview  mGage CPaaS API lets you interact with the CPaaS platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  CPaaS APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible. Major releases are not, please be careful when upgrading.  A new account is pinned to the latest version at the time of first request. By default every request sent CPaaS is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header `api-version`. Note: Specifying this value will not change your pinned version for other calls.  CPaaS also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use `api-version` header for that client version. When using official CPaaS HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Response format  All CPaaS APIs follow a common response format. Each response will have a `meta` field which contains metadata about the response (like the request_uuid).  APIs which return a single object will have a field `data` which contains the object being returned.  APIs which return a list of objects will have a field `objects` which contains the list of objects being returned.  ## Pagination Pagination for list APIs are controlled using query parameters:   - `limit`: Number of objects to be returned   - `offset`: Number of objects to skip before collecting the output list.  These fields are also present in the response under the field `meta`. 

    OpenAPI spec version: 1.0
    Contact: apiteam@mgageindia.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import sys
from setuptools import setup, find_packages

NAME = "cpaas-python"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="cpaas api",
    author_email="apiteam@mgageindia.com",
    url="",
    keywords=["Swagger", "cpaas api"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    # Overview  mGage CPaaS API lets you interact with the CPaaS platform. It allows you to query your account, set up webhooks, send messages and buy phone numbers.  # API and Clients Versioning  CPaaS APIs are versioned using the format vX.Y where X is the major version number and Y is minor. All minor version changes are backwards compatible. Major releases are not, please be careful when upgrading.  A new account is pinned to the latest version at the time of first request. By default every request sent CPaaS is processed using that version, even if there have been subsequent breaking changes. This is done to prevent existing user applications from breaking. You can change the pinned version for your account using the account dashboard. The default API version can be overridden by specifying the header &#x60;api-version&#x60;. Note: Specifying this value will not change your pinned version for other calls.  CPaaS also provides HTTP API clients for all major languages. Release versions of these clients correspond to their API Version supported. Client version vX.Y.Z supports API version vX.Y. HTTP Clients are configured to use &#x60;api-version&#x60; header for that client version. When using official CPaaS HTTP Clients only, you dont need to concern yourself with pinned version. To upgrade your API version simply update the client.  # Common Response format  All CPaaS APIs follow a common response format. Each response will have a &#x60;meta&#x60; field which contains metadata about the response (like the request_uuid).  APIs which return a single object will have a field &#x60;data&#x60; which contains the object being returned.  APIs which return a list of objects will have a field &#x60;objects&#x60; which contains the list of objects being returned.  ## Pagination Pagination for list APIs are controlled using query parameters:   - &#x60;limit&#x60;: Number of objects to be returned   - &#x60;offset&#x60;: Number of objects to skip before collecting the output list.  These fields are also present in the response under the field &#x60;meta&#x60;. 
    """
)
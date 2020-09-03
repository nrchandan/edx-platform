"""
Viewset for auth/saml/v0/saml_configuration
"""

from django.shortcuts import get_object_or_404
from edx_rbac.mixins import PermissionRequiredMixin
from edx_rest_framework_extensions.auth.jwt.authentication import JwtAuthentication
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import ParseError, ValidationError

from enterprise.models import EnterpriseCustomerIdentityProvider, EnterpriseCustomer
from third_party_auth.utils import validate_uuid4_string

from ..models import SAMLConfiguration
from .serializers import SAMLConfigurationSerializer


class SAMLConfigurationMixin(object):
    authentication_classes = (JwtAuthentication, SessionAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = SAMLConfigurationSerializer


class SAMLConfigurationViewSet(SAMLConfigurationMixin, viewsets.ModelViewSet):
    """
    A View to handle SAMLConfiguration GETs

    Usage:
        GET /auth/saml/v0/saml_configuration/
    """

    def get_queryset(self):
        """
        Find and return all saml configurations that are listed as public.
        """
        return SAMLConfiguration.objects.current_set().filter(is_public=True)

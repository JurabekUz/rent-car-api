from rest_framework import generics

from company_app.serializers.compserializers import ( CompDataSlz,
                                                    AboutCompanySlz,
                                                    SocialAccountsSlz )

from company_app.models.company_data import CompanyData, AboutCompany, SocialAccounts


class CompDataList(generics.ListAPIView):
    model = CompanyData
    serializer_class = CompDataSlz
    queryset = CompanyData.objects.all()

class AboutCompanyList(generics.ListAPIView):
    model = AboutCompany
    serializer_class = AboutCompanySlz
    queryset = AboutCompany.objects.all()

class SocialAccountList(generics.ListAPIView):
    model = SocialAccounts
    serializer_class = SocialAccountsSlz
    queryset = SocialAccounts.objects.all()


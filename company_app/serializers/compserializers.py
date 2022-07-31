from rest_framework.serializers import ModelSerializer

from company_app.models.company_data import CompanyData, AboutCompany, SocialAccounts

class CompDataSlz(ModelSerializer):
    class Meta:
        model = CompanyData
        fields = ('location',  'phone', 'email')

class AboutCompanySlz(ModelSerializer):
    class Meta:
        model = AboutCompany
        fields = ('about', 'brif_info', 'year_exp', 'yotal_cars', 'customers', 'total_branchs')


class SocialAccountsSlz(ModelSerializer):
    class Meta:
        model = SocialAccounts
        fields = ( 'website', 'twitter', 'facebook', 'telegram', 'tiktok', 'instagram')
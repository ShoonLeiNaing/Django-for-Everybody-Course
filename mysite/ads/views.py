from ads.models import Ad
from ads.owner import OwnerListView,OwnerDetailView,OwnerCreateView,OwnerUpdateView,OwnerDeleteView

class AdListView(OwnerListView):
    template_name="ads/ads_list.html"
    model = Ad


class AdDetailView(OwnerDetailView):
    template_name="ads/ads_detail.html"
    model = Ad

class AdCreateView(OwnerCreateView):
    template_name="ads/ads_form.html"
    model = Ad
    fields = ['title','price', 'text']

class AdUpdateView(OwnerUpdateView):
    template_name="ads/ads_form.html"
    model = Ad
    fields = ['title','price', 'text']

class AdDeleteView(OwnerDeleteView):
    template_name="ads/ads_confirm_delete.html"
    model = Ad


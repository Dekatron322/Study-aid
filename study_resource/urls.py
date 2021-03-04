from django.urls import path
from . import views

app_name = "study_resource"

urlpatterns = [
	
	path("share-study-resource/", views.ShareResourceView, name="share_resource"),
	path("study-resource-detail/<int:id>/", views.ResourceDetailView, name="resource_detail"),
	path("contribute-to-ebook/<int:id>/", views.ContributeFileResourceView, name="contribute_ebook"),
	path("contribute-to-resource/<int:id>/", views.ContributeResourceView, name="contribute_resource"),
	path("contribute-to-link/<int:id>/", views.ContributeLinkResourceView, name="contribute_link"),
	path("chat-form/", views.ChatForumView, name="chat_forum")


]

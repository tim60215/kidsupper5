from __future__ import unicode_literals

from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from mezzanine.core.views import direct_to_template
from messurements.views import PressureListView, WeightListView, PressureWeightView, WeightFormView, AllView, UserProfileListView, BasicListView, SleepListView, ExerciseListView, MealListView, AllView


admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = i18n_patterns("",
    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    ("^admin/", include(admin.site.urls)),
)
urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^weight/list/$', login_required(WeightListView.as_view()), name="weight-list"),
    url(r'^pressure/list/$', login_required(PressureListView.as_view()), name="pressure-list"),
    url(r'^height/list/$', login_required(UserProfileListView.as_view()), name="height-list"),
    url(r'^sleep/list/$', login_required(SleepListView.as_view()), name="sleep-list"),
    url(r'^exercise/list/$', login_required(ExerciseListView.as_view()), name="exercise-list"),
    url(r'^meal/list/$', login_required(MealListView.as_view()), name="meal-list"),
    url(r'^messurement/add/today/$', PressureWeightView, name="add_values"),
    url(r'^messurement/add/$', AllView, name="new_values"),
    # TODO: For some reasons I'm not able to get it running with reverse'
    url(r'^messurement/add/weight/$', login_required(WeightFormView.as_view(template_name='messurements/weight_form.html', success_url='/dashboard/')), name="add_weight"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="home"),
    url(r'^dashboard/$', TemplateView.as_view(template_name='dashboard.html'), name="user_dashboard")
)

urlpatterns += patterns('',

    # Cartridge URLs.
    ("^shop/", include("cartridge.shop.urls")),
    url("^account/orders/$", "cartridge.shop.views.order_history",
        name="shop_order_history"),

    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    url("^$", direct_to_template, {"template": "index.html"}, name="home"),

    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part. Make
    # sure to uncheck all templates for the "show in menus" field
    # when you create the page, since the link to the homepage is
    # always hard-coded into all the page menus that display navigation
    # on the site. Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/index.html" can
    # be used.

    # url("^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.

    # url("^$", "mezzanine.blog.views.blog_post_list", name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    ("^", include("mezzanine.urls")),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # ("^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"

from django.contrib.syndication.views import Feed


class LatestEntriesFeed(Feed):
    title = "NDbits site news"
    link = "/"
    description = "New stories and additions to the NDbits site."

    def items(self):
        return NewsItem.objects.order_by('-pub_date')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    # item_link is only needed if NewsItem has no get_absolute_url method.
    def item_link(self, item):
        return reverse('news-item', args=[item.pk])
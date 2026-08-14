from tethys_sdk.base import TethysAppBase, url_map_maker

class Regionaldrought(TethysAppBase):
    """
    Tethys app class for Regionaldrought.
    """

    name = 'Regional Drought Monitoring and Outlook System for South Asia'
    description = ''
    package = 'regionaldrought'  # WARNING: Do not change this value
    # index = 'home'
    index = 'Outlook'
    icon = f'{package}/images/icon.gif'
    root_url = 'regionaldrought'
    color = '#c23616'
    tags = 'Drought-Watch'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='CurrentHome',
                url='regionaldrought/current',
                controller='regionaldrought.controllers.Current.home'
            ),
            UrlMap(
                name='Outlook',
                url='regionaldrought',
                controller='regionaldrought.controllers.Outlook.home'
            ),
            UrlMap(
                name='OutlookHome',
                url='regionaldrought/outlook',
                controller='regionaldrought.controllers.Outlook.home'
            ),
            UrlMap(
                name='getSpatialAverage',
                url='regionaldrought/ajax/getspatialaverage',
                controller='regionaldrought.ajax.get_spatialaverage',
            ),
            UrlMap(
                name='getSpatialAverageCurrent',
                url='regionaldrought/ajax/getspatialaveragecurrent',
                controller='regionaldrought.ajax.get_spatialaveragecurrent',
            ),
            UrlMap(
                name='slicedfromcatalog',
                url='regionaldrought/slicedfromcatalog',
                controller='regionaldrought.controllers.Common.SlicedFromCatalog',
            )
        )

        return url_maps
module.exports = {
    pages: {
        activity_timeline: {
            entry: 'src/modules/activity_timeline/activity_timeline.js',
            template: 'public/activity_timeline.html',
            filename: 'activity_timeline.html'
        },
        activity: {
            entry: 'src/modules/activity/activity.js',
            template: 'public/activity.html',
            filename: 'activity.html'
        },
        invasion_timeline: {
            entry: 'src/modules/invasion_timeline/invasion_timeline.js',
            template: 'public/invasion_timeline.html',
            filename: 'invasion_timeline.html'
        },
        entry: {
            entry: 'src/modules/entry/entry.js',
            template: 'public/entry.html',
            filename: 'entry.html'
        },
        entry_search: {
            entry: 'src/modules/entry_search/entry_search.js',
            template: 'public/entry_search.html',
            filename: 'entry_search.html'
        },
        settings: {
            entry: 'src/modules/settings/settings.js',
            template: 'public/settings.html',
            filename: 'settings.html'
        }
    }
}
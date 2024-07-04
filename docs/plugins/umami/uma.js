(function () {
    let install = function (hook, vm) {
        if (!$docsify.umami_src) {
            console.error('[Docsify] Umami src is required.');
            return;
        }
        if (!$docsify.umami_id) {
            console.error('[Docsify] Umami id is required.');
            return;
        }

        // Invoked one time when the docsify instance has mounted on the DOM
        hook.mounted(function () {
            let script = document.createElement('script');
            script.defer = true;
            script.src = $docsify.umami_url;
            script.setAttribute('data-website-id', $docsify.umami_id);
            document.head.appendChild(script);
        });

        // Invoked on each page load before new markdown is transformed to HTML.
        hook.beforeEach(function (markdown) {
            umami.track();
        });
    };

    $docsify.plugins = [].concat(install, $docsify.plugins);

}());

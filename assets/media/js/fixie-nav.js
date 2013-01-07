$(document).ready(function(){

    var toggleFixieNav = function toggleFixieNav(e) {
        $('#fixie-nav-expanded').toggleClass('hidden');
    };

    $('#fixie-nav').hover(
        function toggleFixieNav(e) {
            $('#fixie-nav-expanded').toggleClass('hidden');
        },
        function toggleFixieNav(e) {
            $('#fixie-nav-expanded').toggleClass('hidden');
        }
    );

    var populateContactLink = function(){
        var rounds = ['oceans_11', 'evilserver', 'feynman', 'get_smart', 'indiana', 'sneakers', 'rubik'];
        var location = window.location.pathname.split('/');
        if (rounds.indexOf(location[1]) > -1) {
            var roundName = location[1];
            var puzzleName = location[2];
            var getString = '?round=' + roundName;
            if (puzzleName) {
                getString = getString + '&puzzle=' + puzzleName;
            }
            var contactLink = $('#contact-hq-link')[0].href;
            $('#contact-hq-link').attr('href', contactLink + getString);
        }
    };

    populateContactLink();
});

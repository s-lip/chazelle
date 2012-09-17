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
    
});

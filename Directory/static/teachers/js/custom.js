// static/teachers/js/custom.js
$(document).ready(function() {
    $('#filter-by-last-name').on('change', function() {
        var letter = $(this).val();
        $.get('/teachers/filter/last_name/' + letter, function(data) {
            $('#teacher-list').html(data.teachers);
        });
    });

    $('#filter-by-subject').on('change', function() {
        var subject = $(this).val();
        $.get('/teachers/filter/subject/' + subject, function(data) {
            $('#teacher-list').html(data.teachers);
        });
    });
});

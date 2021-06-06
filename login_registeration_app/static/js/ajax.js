$(function () {
    $("#search").autocomplete({
        source: "{% url 'autocomplete' %}",
        minLength: 1
    });
});
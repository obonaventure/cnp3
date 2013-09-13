
$(function() {
    if (typeof $nmbr_prop == 'undefined') {
        $nmbr_prop = Infinity;
    }
    $('.comment').hide();
    $('ul.positive').before('<ul class="proposals"></ul>');
    $('ul.positive').each(function(index) {
        $(this).shuffle().children('li').first()
            .prependTo($(this).parent().children('ul.proposals'))
            .attr('class', 'correct');
    });
    $('ul.negative').each(function(index) {
        $(this).shuffle();
        $(this).children('li').slice(0, $nmbr_prop-1).each(function(index) {
            $(this)
            .prependTo($(this).parent().parent().children('ul.proposals'))
            .attr('class', 'false');
        });
    });
    $('ul.proposals').each(function(index) {
        $(this).shuffle();
        $('<input type="radio" name="' + $(this).parent().attr('id') + '">').prependTo($(this).children('li'));
    });
    $('ul.positive').hide();
    $('ul.negative').hide();
    $('body').append('<div id="checker" class="checker"><h1>Check your answers</h1><input type="submit" value="Check" id="verifier"></div>');
    $('#verifier').click(function () {
        $('.comment').hide();
        $('.checkmark').remove();
        $('.result').remove();
        $('li.false input:checked').parent().prepend('<img class="checkmark" src="images/false.png" style="display: none;"></img>');
        $('li.correct input:checked').parent().prepend('<img class="checkmark" src="images/correct.png" style="display: none;"></img>');
        $('.checkmark').show();
        $('input:checked').parent().children('.comment').show('slow');
        $('#checker').append('<div class="result">Your score is ' +
                            $('li.correct input:checked').length + '/' +
                            $('ul.proposals').length + '</div>');
    });
    $('pre.literal-block').addClass('prettyprint');
    prettyPrint();
});


var score;

var translations = {
    fr: {
        score: 'Votre score est de',
        inginious_success: 'Tout s\'est bien passé',
        request_fail: 'La requête a échoué'
    },
    en: {
        score: 'You have a score of ',
        inginious_success: 'Everything wen well',
        request_fail: 'The request failed'
    }
};

$(function() {
    $('input:checked').prop('checked', false);
    $('.question').each(shuffle);
    $('#submit').click(submit);
});

function shuffle(index) {
    var nb_pos = $(this).children('.nb_pos').val();
    var nb_prop = $(this).children('.nb_prop').val();
    $(this).shuffle();
    $(this).children('.positive').slice(nb_pos).remove();
    $(this).children('.negative').slice(nb_prop-nb_pos).remove();
    $(this).children('.query').prependTo($(this));
    $(this).children('h2').prependTo($(this));
}

function submit() {
    check();
    log();
//OB : remove inginious
//    inginious();
}

function check() {
    score = 0;
    $('.comment').hide();
    $('.checkmark').remove();
    $('.result').remove();
    $('.query .comment').show('slow');
    $('input:checked').siblings().children('.comment').show('slow');
    $('.textbox .comment').show('slow');
    $('.question').each(compute_score);
    $('#checker').append('<div class="result">' + translations[language]['score'] + ' ' +
                        score + '/' +
                        $('.positive').parent().length + '</div>');
}

function compute_score() {
    if ($(this).children('.textbox').length > 0) {
        return;
    }
    var nb_pos = $(this).children('.nb_pos').val();
    var nb_pos_checked = $(this).children('.positive').children('input:checked').length;
    var nb_neg_checked = $(this).children('.negative').children('input:checked').length;
    // for sphinx
    var pos_img = '<img class="checkmark" src="'+DOCUMENTATION_OPTIONS.URL_ROOT+'/_static/true.png" />';
    var neg_img = '<img class="checkmark" src="'+DOCUMENTATION_OPTIONS.URL_ROOT+'/_static/false.png" />';
    var scored = false;
    if (nb_neg_checked == 0 && nb_pos_checked == nb_pos) {
        scored = true;
        score++;
    }
    if (nb_pos > 1 || nb_pos_checked + nb_neg_checked == 0) {
        if (scored) {
            $(this).children('.query').after(pos_img);
        } else {
            $(this).children('.query').after(neg_img);
        }
    } else {
        $(this).children('.positive').children('input:checked').after(pos_img);
        $(this).children('.negative').children('input:checked').after(neg_img);
    }
}

function log() {
    if (upload_url != '') {
        var json = makeJson();
        if (!$.isEmptyObject(json.questions)) {
            $.ajax({
                type: 'POST',
                url: upload_url,
                data: JSON.stringify(json)
            });
        }
    }
}

function makeJson() {
    var json = {
        html_title: html_title,
        title: title,
        hash: hash,
        questions: {}
    };
    $('.question').each(function(index) {
        var query = $(this).children('.query');
        query.children('.comment').removeAttr('style');
        query = query.html();
        $comment = $(this).children('.textbox').children('.comment');
        if ($comment.length > 0) {
            query += "<div class='comment'>" + $comment.html() + "</div>";
        }
        var $input = $(this).children().children('input:checked');
        var answers = [];
        while ($input.length > 0) {
            $content = $input.siblings('.content');
            $content.children('.comment').removeAttr('style');
            answers.push($content.html());
            $input = $input.slice(1);
        }
        var textbox = $(this).children('.textbox').children('textarea').val();
        var isTextbox = false;
        if (textbox != undefined && textbox != '') {
            answers.push(textbox);
            isTextbox = true;
        }
        if (answers.length > 0) {
            json.questions[$(this).attr('id')] = {
                title: $(this).prev().text().slice(0, -1),
                query: query,
                answers: answers,
                textbox: isTextbox
            };
        }
    });
    return json;
}

function inginious() {
    if (inginious_url && inginious_url != '' && task_id != '') {
        var input = makeInginiousInput();
        $('#results').hide().children().remove();
        $('.problem').remove();
        $.ajax({
            type: 'POST',
            url: inginious_url,
            data: {taskid: task_id, input: JSON.stringify(input)},
            dataType: 'json'
        }).done(function(result) {
            if (result['status'] == 'error') {
                result['result'] = 'error';
                result['text'] = result['status_message'];
            }
            if (result['text'] == '') {
                result['text'] = translations[language]['inginious_success'];
            }
            $('#results').append("<p class='" + result['result'] + "'>INGInious: " + result['text'] + "</p>");
            for (var key in result['problems']) {
                $('#' + key).prepend('<p class="problem">INGInious: ' + result['problems'][key] + '</p>');
            }
        }).fail(function(e) {
            $('#results').append("<p class='request-failed'>INGInious: " + translations[language]['request_failed'] + "</p>");
        }).always(function() {
            $('#results').show();
        });
    }
}

function makeInginiousInput() {
    var input = {};
    $('.question.inginious').each(function(index) {
        choices = [];
        $input = $(this).children().children('input:checked');
        while($input.length > 0) {
            choices.push(parseInt($input.parent().attr('id')));
            $input = $input.slice(1);
        }
        if (choices.length == 0) {
            $textbox = $(this).children('.textbox').children('textarea');
            if ($textbox.length > 0) {
                choices = $textbox.val();
            }
        }
        input[$(this).attr('id')] = choices;
    });
    return input;
}

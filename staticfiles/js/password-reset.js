$(() => {
    /* ▼▼ デフォルトのテキストの非表示 ▼▼ */
    $('form ul').each((i, elem) => {
        if($(elem).hasClass('errorlist')) {
            return true;
        } else {
            $(elem).remove();
        }
    });
});

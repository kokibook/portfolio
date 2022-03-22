$(() => {
    // 選択したファイル名を表示
    $('input[id=id_image]').change(function() {
        $('#judge-photo-cover').val($(this).val().replace("C:\\fakepath\\", ""));
    });
});
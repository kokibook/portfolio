$(() => {
    // 画像のURLを取得
    const imageUrl = $('.update-form-field a').attr('href');

    // 画像の要素を作成 & 追加
   const img = $("<img />", {
        src: imageUrl,
    });
    $('.update-form .update-form-label:first').before(img);

    // 元の画像部分の削除
    const $lastUpdateFormLabel = $('.update-form .update-form-label:last');

    $lastUpdateFormLabel.find('a').remove();
    const text = $lastUpdateFormLabel.html();
    $lastUpdateFormLabel.html(
        text.replace('現在: <br>' ,'')
            .replace('変更:', '')
    )

    // 選択したファイル名を表示
    $('input[id=id_person_image]').change(function() {
        $('#update-photo-cover').val($(this).val().replace("C:\\fakepath\\", ""));
    });

});
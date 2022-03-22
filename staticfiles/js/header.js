'use strict';

$(() => {
    // ロゴをタップした時にページ上部へ戻る
    $('.header-logo').click( () => {
        $('html, body').animate({
            'scrollTop': 0
        }, 300);
    });

    // ユーザー名をタップした時のメニューの挙動
    $('.user-login-name').click((e) => {
        const _this = e.currentTarget;
        const $userSettings = $('.user-settings');

        if ($userSettings.hasClass('settings-is-open')) {
            $userSettings.removeClass('settings-is-open');
            const text = '▼';
            $(_this).find('span').text(text);
        } else {
            $userSettings.addClass('settings-is-open');
            const text = '▲';
            $(_this).find('span').text(text);
        }
    });

    // 範囲外をタップした時にメニューを非表示
    $(document).click((e) => {
        const target = '.user-content';

        if(!$(e.target).closest(target).length) {
            const $userSettings = $('.user-settings');

            if ($userSettings.hasClass('settings-is-open')) {
                $userSettings.removeClass('settings-is-open');
                const text = '▼';
                $('.user-content').find('span').text(text);
            }
        }
    });

    // ハンバーガーメニューの挙動
    $('#hamburger-menu-btn').click((e) => {
        const _this = e.currentTarget;
        const $hamburgerMenuWrapper = $('#hamburger-menu-wrapper');

        if($(_this).hasClass('active')) {
            $(_this).removeClass('active');
            $hamburgerMenuWrapper.removeClass('panelactive');
        } else {
            $(_this).addClass('active');
            $hamburgerMenuWrapper.addClass('panelactive');
        }
    });
    
});
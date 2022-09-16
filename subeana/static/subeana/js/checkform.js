var isfirstget = true;
var isfirstinfo = true
async function checksong(basedir) {
    if (isfirstget) {
        res = await fetch(basedir + "/subeana/api/song/?format=json");
        songjson = await res.json();
        isfirstget = false;
    }
    formtitle = document.getElementById("title").value
    song = songjson.find((v) => v.title == formtitle);      // jsonから歌詞を検索
    if (song != null) {     // 記事があった場合
        toastr.options = {
            "closeButton": true,
            "debug": false,
            "newestOnTop": false,
            "progressBar": true,
            "positionClass": "toast-bottom-right",
            "preventDuplicates": false,
            "onclick": null,
            "timeOut": "5000",
            "extendedTimeOut": "0",
            "showEasing": "swing",
            "hideEasing": "linear",
        }
        
        if (song.lyrics == "") {
            toastr.info(song.title + "の記事は登録済ですが、歌詞が登録されていません")
        } else {
            toastr.info(song.title + "の歌詞は登録済です。")
        }
        if (isfirstinfo) {
            toastr.info("送信ボタンを押すと元の記事を上書きします")
            isfirstinfo = false
        }
    }
};

function checkform() {
    formchannel = document.getElementById("channel").value
    formimitate = document.getElementById("imitate").value
    formsubmit = document.getElementById("submit")
    if ((formchannel != "") && (formimitate != "選択してください")) {
        formsubmit.disabled = false;
    } else {
        formsubmit.disabled = true;
    }
}
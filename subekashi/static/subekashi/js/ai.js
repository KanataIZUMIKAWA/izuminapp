async function setscore(basedir, id, score) {
    // res = await fetch(basedir + "/api/ai/" + id + "?format=json");
    // json_ai = await res.json();

    // users = json_ai.users.split(",");
    // if (!users.includes(username)) {
    //     users.push(username);
    //     users = users.join(",");
    //     json_ai.users = users;
    //     json_ai.poeple = Number(json_ai.poeple) + 1;
    //     json_ai.score = Number(json_ai.score) + score;

    //     res = await fetch(
    //         basedir + "/api/ai/" + id + "/?format=json",
    //         {
    //             method: "PUT",
    //             headers: {
    //                 'Content-Type': 'application/json'
    //             },
    //             body: json_ai
    //         }
    //     );
    // } else {
    //     toastr.options = {
    //         "closeButton": true,
    //         "debug": false,
    //         "newestOnTop": false,
    //         "progressBar": true,
    //         "positionClass": "toast-bottom-right",
    //         "preventDuplicates": false,
    //         "onclick": null,
    //         "timeOut": "10000",
    //         "extendedTimeOut": "0",
    //         "showEasing": "swing",
    //         "hideEasing": "linear",
    //     }

    //     toastr.warning("この行は既に評価済です。")
    // }
    res = await fetch(
        basedir + "/api/ai/" + id + "/?format=json",
        {
            method: "PUT",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(
                {
                    "score": score,
                }
            )
        }
    );
}


function devinput(basedir, id, score) {
    for (s = 1; s <= 5; s++) {
        radioEle = document.getElementById(String(id) + String(s));
        radioEle.checked = false;
    }

    radioEle = document.getElementById(String(id) + String(score));
    radioEle.checked = true;
    setscore(basedir, id, score);
}
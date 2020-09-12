onmessage = function (e) {
    [text, key, fastSearchStartIndex, fastSearchEndIndex] = e.data;
    console.log("Decipher: " + text);
    text = text.toUpperCase();
    var keys = Object.keys(key);
    var usedLetters = "";
    for (var i = 0; i < keys.length; i++) {
        text = text.replaceAll(keys[i].toUpperCase(), key[keys[i]]);
        usedLetters += key[keys[i]];
    }
    textLength = text.length;
    decipher(text, "", "", usedLetters, 0);
    postMessage([true, "!", 0]);
};

var fastSearchStartIndex, fastSearchEndIndex, textLength;

const alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"];

var invalidCombos = ["au", "av", "bb", "bc", "bd", "bf", "bg", "bh", "bj", "bk", "bl", "bm", "bn", "bp", "bq", "br", "bs", "bt", "bv", "bw", "bx", "by", "bz", "cb", "cc", "cd", "cf", "cg", "cj", "ck", "cl", "cm", "cn", "cp", "cq", "cr", "cs", "ct", "cv", "cw", "cx", "cy", "cz", "db", "dc", "dd", "df", "dg", "dh", "dj", "dk", "dl", "dm", "dn", "dp", "dq", "dr", "ds", "dt", "dv", "dw", "dx", "dy", "dz", "eu", "ev", "fb", "fc", "fd", "ff", "fg", "fh", "fi", "fj", "fk", "fl", "fm", "fn", "fp", "fq", "fr", "fs", "ft", "fv", "fw", "fx", "fy", "fz", "gi", "gv", "hb", "hc", "hd", "hf", "hg", "hh", "hj", "hk", "hl", "hm", "hp", "hq", "hr", "hs", "ht", "hv", "hw", "hx", "hy", "hz", "ii", "iv", "ja", "jb", "jc", "jd", "je", "jf", "jg", "jh", "jj", "jk", "jl", "jm", "jn", "jo", "jp", "jq", "jr", "js", "jt", "jv", "jw", "jx", "jy", "jz", "kb", "kc", "kd", "kf", "kg", "kh", "ki", "kj", "kk", "kl", "km", "kn", "kp", "kq", "kr", "ks", "kt", "kv", "kw", "kx", "ky", "kz", "lb", "lc", "ld", "lf", "lg", "lh", "lj", "lk", "ll", "lm", "ln", "lp", "lq", "lr", "ls", "lt", "lw", "lx", "ly", "lz", "mb", "mc", "md", "mf", "mg", "mh", "mj", "mk", "ml", "mm", "mn", "mp", "mq", "mr", "ms", "mt", "mv", "mw", "mx", "my", "mz", "oi", "ov", "pb", "pc", "pd", "pf", "pg", "ph", "pj", "pk", "pl", "pm", "pn", "pp", "pq", "pr", "ps", "pt", "pv", "pw", "px", "py", "pz", "qa", "qb", "qc", "qd", "qe", "qf", "qg", "qh", "qj", "qk", "ql", "qm", "qn", "qo", "qp", "qq", "qr", "qs", "qt", "qv", "qw", "qx", "qy", "qz", "rv", "sb", "sc", "sd", "sf", "sg", "sj", "sk", "sl", "sm", "sn", "sp", "sq", "sr", "ss", "st", "sv", "sw", "sx", "sy", "sz", "tb", "tc", "td", "tf", "tg", "th", "tj", "tk", "tl", "tm", "tn", "tp", "tq", "tr", "ts", "tt", "tv", "tw", "tx", "ty", "tz", "uu", "uv", "vi", "vu", "vv", "wb", "wc", "wd", "wf", "wg", "wh", "wi", "wj", "wk", "wl", "wm", "wn", "wp", "wq", "wr", "ws", "wt", "wv", "ww", "wx", "wy", "wz", "xa", "xb", "xc", "xd", "xe", "xf", "xg", "xh", "xj", "xk", "xl", "xm", "xn", "xo", "xp", "xq", "xr", "xs", "xt", "xv", "xw", "xx", "xy", "xz", "yb", "yc", "yd", "yf", "yg", "yh", "yj", "yk", "yl", "ym", "yn", "yp", "yq", "yr", "ys", "yt", "yv", "yw", "yx", "yy", "yz", "zb", "zc", "zd", "zf", "zg", "zj", "zk", "zl", "zm", "zn", "zp", "zq", "zr", "zs", "zt", "zv", "zw", "zx", "zy", "zz"];

var validCombos = ["aa", "ab", "ac", "ad", "ae", "af", "ag", "ah", "ai", "aj", "ak", "al", "am", "an", "ao", "ap", "aq", "ar", "as", "at", "aw", "ax", "ay", "az", "ba", "be", "bi", "bo", "bu", "ca", "ce", "ch", "ci", "co", "cu", "da", "de", "di", "do", "du", "ea", "eb", "ec", "ed", "ee", "ef", "eg", "eh", "ei", "ej", "ek", "el", "em", "en", "eo", "ep", "eq", "er", "es", "et", "ew", "ex", "ey", "ez", "fa", "fe", "fo", "fu", "ga", "gb", "gc", "gd", "ge", "gf", "gg", "gh", "gj", "gk", "gl", "gm", "gn", "go", "gp", "gq", "gr", "gs", "gt", "gu", "gw", "gx", "gy", "gz", "ha", "he", "hi", "hn", "ho", "hu", "ia", "ib", "ic", "id", "ie", "if", "ig", "ih", "ij", "ik", "il", "im", "in", "io", "ip", "iq", "ir", "is", "it", "iu", "iw", "ix", "iy", "iz", "ji", "ju", "ka", "ke", "ko", "ku", "la", "le", "li", "lo", "lu", "lv", "ma", "me", "mi", "mo", "mu", "na", "nb", "nc", "nd", "ne", "nf", "ng", "nh", "ni", "nj", "nk", "nl", "nm", "nn", "no", "np", "nq", "nr", "ns", "nt", "nu", "nv", "nw", "nx", "ny", "nz", "oa", "ob", "oc", "od", "oe", "of", "og", "oh", "oj", "ok", "ol", "om", "on", "oo", "op", "oq", "or", "os", "ot", "ou", "ow", "ox", "oy", "oz", "pa", "pe", "pi", "po", "pu", "qi", "qu", "ra", "rb", "rc", "rd", "re", "rf", "rg", "rh", "ri", "rj", "rk", "rl", "rm", "rn", "ro", "rp", "rq", "rr", "rs", "rt", "ru", "rw", "rx", "ry", "rz", "sa", "se", "sh", "si", "so", "su", "ta", "te", "ti", "to", "tu", "ua", "ub", "uc", "ud", "ue", "uf", "ug", "uh", "ui", "uj", "uk", "ul", "um", "un", "uo", "up", "uq", "ur", "us", "ut", "uw", "ux", "uy", "uz", "va", "vb", "vc", "vd", "ve", "vf", "vg", "vh", "vj", "vk", "vl", "vm", "vn", "vo", "vp", "vq", "vr", "vs", "vt", "vw", "vx", "vy", "vz", "wa", "we", "wo", "wu", "xi", "xu", "ya", "ye", "yi", "yo", "yu", "za", "ze", "zh", "zi", "zo", "zu"];

const shortestPinyin = ["a", "e", "o", "ai", "an", "ba", "bi", "bo", "bu", "ca", "ce", "ci", "cu", "da", "de", "di", "du", "ei", "en", "er", "fa", "fo", "fu", "ga", "ge", "gu", "ha", "he", "hu", "ji", "ju", "ka", "ke", "ku", "la", "le", "li", "lo", "lu", "lv", "ma", "me", "mi", "mo", "mu", "na", "ne", "ni", "nu", "nv", "ou", "pa", "pi", "po", "pu", "qi", "qu", "re", "ri", "ru", "sa", "se", "si", "su", "ta", "te", "ti", "tu", "wa", "wo", "wu", "xi", "xu", "ya", "ye", "yi", "yo", "yu", "za", "ze", "zi", "zu", "ang", "bai", "ban", "bei", "ben", "bin", "cai", "can", "cen", "cha", "che", "chi", "chu", "cou", "cui", "cun", "dai", "dan", "dei", "den", "diu", "dou", "dui", "dun", "fan", "fei", "fen", "fou", "gai", "gan", "gei", "gen", "gou", "gui", "gun", "hai", "han", "hei", "hen", "hou", "hui", "hun", "jin", "jiu", "jun", "kai", "kan", "kei", "ken", "kou", "kui", "kun", "lai", "lan", "lei", "lin", "liu", "lou", "lun", "mai", "man", "mei", "men", "min", "miu", "mou", "nai", "nan", "nei", "nen", "nin", "niu", "pai", "pan", "pei", "pen", "pin", "pou", "qin", "qiu", "qun", "ran", "rao", "ren", "rou", "rui", "run", "sai", "san", "sen", "sha", "she", "shi", "shu", "sou", "sui", "sun", "tai", "tan", "tou", "tui", "tun", "wai", "wan", "wei", "wen", "xin", "xiu", "xun", "yan", "yin", "you", "yun", "zai", "zan", "zei", "zen", "zha", "zhe", "zhi", "zhu", "zou", "zui", "zun", "bang", "beng", "bing", "cang", "ceng", "chai", "chan", "chen", "chou", "chui", "chun", "cong", "dang", "deng", "ding", "dong", "fang", "feng", "gang", "geng", "gong", "hang", "heng", "hong", "jing", "kang", "keng", "kong", "lang", "leng", "ling", "long", "mang", "meng", "ming", "nang", "neng", "ning", "nong", "pang", "peng", "ping", "qing", "rang", "reng", "rong", "sang", "seng", "shai", "shan", "shei", "shen", "shou", "shui", "shun", "song", "tang", "teng", "ting", "tong", "wang", "weng", "xing", "yang", "ying", "yong", "zang", "zeng", "zhai", "zhan", "zhei", "zhen", "zhou", "zhui", "zhun", "zong", "chang", "cheng", "chong", "jiong", "qiong", "shang", "sheng", "xiong", "zhang", "zheng", "zhong"];

const validLetters = [
    ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "w", "x", "y", "z"],
    ["a", "e", "h", "i", "n", "o", "r", "u", "v"],
    ["a", "e", "g", "i", "n", "o", "u"],
    ["g", "i", "n", "u"],
    ["g"]
];

const alpha2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"];
var count = 0;
var quickSkip;

function decipher(text, processedPinyin, pinyinBuffer, usedLetters, currentPos) {
    if (quickSkip) {
        if (currentPos == fastSearchEndIndex) {
            quickSkip = false;
        }
        else if (currentPos <= fastSearchEndIndex + 1) {
            quickSkip = false;
            return;
        } else {
            return;
        }
    }

    count++;

    if (text.length == 0) {
        // all finished
        if (pinyinBuffer.length == 0) {
            quickSkip = true && fastSearchEndIndex >= 0;
            postMessage([true, processedPinyin, count]);
        }
        else {
            postMessage([false, processedPinyin + pinyinBuffer + text, count]);
        }
        count = 0;
        return;
    } else {
        if (count > 1000) {
            postMessage([false, processedPinyin + pinyinBuffer + text, count]);
            count = 0;
        }
    }

    var currentChar = text[0];

    if (alpha2.indexOf(currentChar) >= 0) {
        var letterPos = pinyinBuffer.length;
        if (letterPos >= validLetters.length) {
            return;
        }

        var letters = validLetters[letterPos];

        for (var i = 0; i < letters.length; i++) {
            var currentLetter = letters[i];
            if (usedLetters.indexOf(currentLetter) >= 0) {
                continue;
            }
            var text2 = text.replaceAll(currentChar, currentLetter);
            if (hasInvalidCombos(text2)) {
                continue;
            }
            var usedLetters2 = usedLetters + currentLetter;
            decipher(text2, processedPinyin, pinyinBuffer, usedLetters2, textLength - text2.length);
        }
    }
    else {
        pinyinBuffer += currentChar;
        if (shortestPinyin.indexOf(pinyinBuffer) >= 0) {
            currentPos++;
            decipher(text.slice(1), processedPinyin, pinyinBuffer, usedLetters, currentPos);

            processedPinyin += pinyinBuffer + " ";
            decipher(text.slice(1), processedPinyin, "", usedLetters, currentPos);
        }
        else {
            if (hasPinyinStartsWith(pinyinBuffer)) {
                currentPos++;
                decipher(text.slice(1), processedPinyin, pinyinBuffer, usedLetters, currentPos);
            }
            return;
        }
    }
}

function hasPinyinStartsWith(text) {
    var found = false;
    for (var i = 0; i < shortestPinyin.length; i++) {
        if (shortestPinyin[i].indexOf(text) == 0) {
            found = true;
            return true;
        }
    }
    return false;
}

function hasInvalidCombos(text) {
    for (var i = 0; i < invalidCombos.length; i++) {
        if (text.indexOf(invalidCombos[i]) >= 0) {
            return true;
        }
    }
    return false;
}

function getFirstCapitalLetter(text) {
    for (var i = 0; i < text.length; i++) {
        if (alpha2.indexOf(text[i]) >= 0) {
            return text[i];
        }
    }
    return null;
}
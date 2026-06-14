// 通知
const Toast = Swal.mixin({
  toast: true,
  position: 'top-end',
  showConfirmButton: false,
  timer: 3000,
  timerProgressBar: true,
  didOpen: (toast) => {
    toast.addEventListener('mouseenter', Swal.stopTimer)
    toast.addEventListener('mouseleave', Swal.resumeTimer)
  }
});

// 通知打印
const getcdn = function(){
  let tag = document.getElementById('cdn');
  Toast.fire({
    icon: 'success',
    title: tag.innerText
  })
};

// 疯狂星期四
4 == new Date().getDay() && console.error('KFC Crazy Thursday need ¥50.');

function hex2rgba(hex, opacity = 1.0) {
    let defaults = "rgb(0,0,0)";

    // 移除#号
    if (hex.startsWith("#")) {
        hex = hex.substring(1);
    }

    // 验证Hex格式
    if (!/^([0-9A-F]{3}|[0-9A-F]{6}|[0-9A-F]{8})$/i.test(hex))
        return defaults;

    // 扩展简写形式（如F00 -> FF0000）
    if (hex.length === 3) {
        hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
    }

    // 解析Hex值
    const r = parseInt(hex.substring(0, 2), 16);
    const g = parseInt(hex.substring(2, 4), 16);
    const b = parseInt(hex.substring(4, 6), 16);

    if (opacity && Math.abs(opacity) > 1) opacity = 1.0;

    // 生成RGBA字符串
    const rgba = `rgba(${r}, ${g}, ${b}, ${opacity})`;
    return rgba;
}

(function () {
    var requestAnimationFrame =
        window.requestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.msRequestAnimationFrame ||
        function (callback) {
            window.setTimeout(callback, 1000 / 60);
        };
    window.requestAnimationFrame = requestAnimationFrame;
})();

(function () {
    var flakes = [],
        canvas = document.getElementById("Snow"), //画布ID，与上一步创建的画布对应
        ctx = canvas.getContext("2d"),
        flakeCount = 100, //雪花数量，数值越大雪花数量越多
        mX = -100,
        mY = -100;

    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;

    function snow() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        for (var i = 0; i < flakeCount; i++) {
            var flake = flakes[i],
                x = mX,
                y = mY,
                minDist = 150, //雪花距离鼠标指针的最小值，小于这个距离的雪花将受到鼠标的排斥
                x2 = flake.x,
                y2 = flake.y;

            var dist = Math.sqrt(
                    (x2 - x) * (x2 - x) + (y2 - y) * (y2 - y),
                ),
                dx = x2 - x,
                dy = y2 - y;

            if (dist < minDist) {
                var force = minDist / (dist * dist),
                    xcomp = (x - x2) / dist,
                    ycomp = (y - y2) / dist,
                    deltaV = force / 2;

                flake.velX -= deltaV * xcomp;
                flake.velY -= deltaV * ycomp;
            } else {
                flake.velX *= 0.98;
                if (flake.velY <= flake.speed) {
                    flake.velY = flake.speed;
                }
                flake.velX +=
                    Math.cos((flake.step += 0.05)) * flake.stepSize;
            }

            ctx.fillStyle =
                "rgba(255,255,255," + flake.opacity + ")"; //雪花颜色
            flake.y += flake.velY;
            flake.x += flake.velX;

            if (flake.y >= canvas.height || flake.y <= 0) {
                reset(flake);
            }

            if (flake.x >= canvas.width || flake.x <= 0) {
                reset(flake);
            }

            ctx.beginPath();
            ctx.arc(flake.x, flake.y, flake.size, 0, Math.PI * 2);
            ctx.fill();
        }
        requestAnimationFrame(snow);
    }

    function reset(flake) {
        flake.x = Math.floor(Math.random() * canvas.width);
        flake.y = 0;
        flake.size = Math.random() * 3 + 2; //加号后面的值，雪花大小，为基准值，数值越大雪花越大
        flake.speed = Math.random() * 1 + 0.5; //加号后面的值，雪花速度，为基准值，数值越大雪花速度越快
        flake.velY = flake.speed;
        flake.velX = 0;
        flake.opacity = Math.random() * 0.5 + 0.3; //加号后面的值，为基准值，范围0~1
    }

    function init() {
        for (var i = 0; i < flakeCount; i++) {
            var x = Math.floor(Math.random() * canvas.width),
                y = Math.floor(Math.random() * canvas.height),
                size = Math.random() * 3 + 2, //加号后面的值，雪花大小，为基准值，数值越大雪花越大
                speed = Math.random() * 1 + 0.5, //加号后面的值，雪花速度，为基准值，数值越大雪花速度越快
                opacity = Math.random() * 0.5 + 0.3; //加号后面的值，为基准值，范围0~1

            flakes.push({
                speed: speed,
                velY: speed,
                velX: 0,
                x: x,
                y: y,
                size: size,
                stepSize: (Math.random() / 30) * 1, //乘号后面的值，雪花横移幅度，为基准值，数值越大雪花横移幅度越大，0为竖直下落
                step: 0,
                angle: 180,
                opacity: opacity,
            });
        }

        snow();
    }

    document.addEventListener("mousemove", function (e) {
        ((mX = e.clientX), (mY = e.clientY));
    });
    window.addEventListener("resize", function () {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    });
    init();
})();

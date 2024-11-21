me().on('load', ev => {
    let e = me(ev)
    confetti({
        particleCount: 200,
        spread: 60,
        origin: { y: 0.6 }
    });
})
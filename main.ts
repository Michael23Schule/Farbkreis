let dunkelheit = 196
let rot = dunkelheit
let gruen = 0
let blau = 0
basic.forever(function () {
    for (let Index = 0; Index <= dunkelheit; Index++) {
        gruen = Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
    for (let Index = 0; Index <= dunkelheit; Index++) {
        rot = dunkelheit - Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
    for (let Index = 0; Index <= dunkelheit; Index++) {
        blau = Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
    for (let Index = 0; Index <= dunkelheit; Index++) {
        gruen = dunkelheit - Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
    for (let Index = 0; Index <= dunkelheit; Index++) {
        rot = Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
    for (let Index = 0; Index <= dunkelheit; Index++) {
        blau = dunkelheit - Index
        basic.setLedColor(basic.rgb(rot, gruen, blau))
        basic.pause(100)
    }
})

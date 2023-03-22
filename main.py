dunkelheit = 196
rot = dunkelheit
gruen = 0
blau = 0
pause2 = 5000

def on_forever():
    global gruen, rot, blau
    Index = 0
    while Index <= dunkelheit:
        gruen = Index
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index += 1
    Index2 = 0
    while Index2 <= dunkelheit:
        rot = dunkelheit - Index2
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index2 += 1
    Index3 = 0
    while Index3 <= dunkelheit:
        blau = Index3
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index3 += 1
    Index4 = 0
    while Index4 <= dunkelheit:
        gruen = dunkelheit - Index4
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index4 += 1
    Index5 = 0
    while Index5 <= dunkelheit:
        rot = Index5
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index5 += 1
    Index6 = 0
    while Index6 <= dunkelheit:
        blau = dunkelheit - Index6
        basic.set_led_color(basic.rgb(rot, gruen, blau))
        basic.pause(100)
        Index6 += 1
basic.forever(on_forever)

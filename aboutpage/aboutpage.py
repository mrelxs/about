# pacman about page
# index

import pynecone as pc

style = {
    "#gradient-canvas": {
        "width": "100%",
        "height": "100%",
        "--gradient-color-1": "#c3e4ff",
        "--gradient-color-2": "#6ec3f4",
        "--gradient-color-3": "#eae2ff",  
        "--gradient-color-4": "#b9beff",
    }
}

class State(pc.State):
    """The app state."""

    def redirect_blox(self):
        return pc.redirect("https://www.roblox.com/users/3692305855/profile")
    
    def redirect_guilded(self):
        return pc.console_log("test"); pc.redirect("https://guilded.gg/u/obamium/")

    pass


def index():
    return pc.center(
        pc.vstack(
            pc.heading("pacman", font_size="1.8em", background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)", background_clip="text"),
            pc.text("goofy goober", font_size="1.5em"),
            pc.divider(),
            pc.hstack(
                pc.button(
                    pc.image(src="/guilded.png", width="25px", height="auto"),
                    #border_radius = "1cm",
                    box_shadow = "rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                    #background_image = "linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                    background_image = "white",
                    box_sizing = "border-box",
                    color = "white",
                    on_click = State.redirect_guilded,
                    _hover = {
                        "opacity": 0.75
                    }
                ),
                pc.button(
                    pc.image(src="/blox.png", width="30px", height="auto"),
                    #border_radius = "1cm",
                    box_shadow = "rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                    #background_image = "linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                    background_image = "white",
                    box_sizing = "border-box",
                    color = "white",
                    on_click = State.redirect_blox,
                    _hover = {
                        "opacity": 0.75
                    }
                ),
            )
        ),
    width="100%",
    padding="10.5cm",
    spacing = "2em",
    bg="radial-gradient(circle at 22% 11%,rgba(62, 180, 137,.20),hsla(0,0%,100%,0) 19%)",
    )


# Add state and page to the app.
app = pc.App(state=State, style=style)
app.add_page(index, title="pacman")
app.compile()

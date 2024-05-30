class person:
    healthy = False

    def declarehealthy(self):
        self.healthy = True

johnny = person()
echo = person()

johnny.declarehealthy()
print("Johnny is healthy:", johnny.healthy)
print("Echo is healthy:", echo.healthy)
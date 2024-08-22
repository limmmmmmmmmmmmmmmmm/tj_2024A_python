


class Region :
    def __init__(self,Bname,Tperson,Mperson,Fperson,home):
        self.Bname = Bname
        self.Tperson = int(Tperson)
        self.Mperson = int(Mperson)
        self.Fperson = int(Fperson)
        self.home = int(home)


    def __repr__(self):
        return (f"BuPyeong(Bname={self.Bname}),Tperson='{self.Tperson}', Mperson={self.Mperson}, Fperson={self.Fperson},"
                f" home={self.home}")


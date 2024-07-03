import importlib

try:
    # from brother import bro as imp_bro
    from pyimp.myfamily.brother import bro as imp_bro
except Exception as e:
    print("0) error: fail to import from dir")
    print(f"{e}")

try:
    from .. import fath as imp_fath
except Exception as e:
    print("1) error: fail to import from above dir")
    print(f"{e}")


def main():
    print("the main is running\n")
    print("## import_module from dir ##")

    try:
        bro_module = importlib.import_module("pyimp.myfamily.brother.bro")
        instance = bro_module.Brother()
        instance.print()
    except:
        print("2) error: fail to import_module brother.bro")
    else:
        print("2) success!")
    finally:
        print("")

    print("## import from dir ##")
    try:
        instance = imp_bro.Brother()
        instance.print()
    except:
        print("3) error: fail to import_module brother.bro")
    else:
        print("3) success!")
    finally:
        print("")

    print("## import_module 1 from above dir ##")
    try:
        fath_module = importlib.import_module("fath", "..")
        instance = fath_module.Father()
        instance.print()
    except:
        print("4) error: fail 1 to import_module ..\\fath.py")
    else:
        print("4) success!")
    finally:
        print("")

    print("## import_module 2 from above dir ##")
    try:
        fath_module = importlib.import_module("..fath")
        instance = fath_module.Father()
        instance.print()
    except:
        print("5) error: fail 2 to import_module ..\\fath.py")
    else:
        print("5) success!")
    finally:
        print("")

    print("## import from above dir ##")

    try:
        from pyimp import fath as imp_fath
        module = imp_fath.Father()
        module.print()
    except:
        print("6) error: fail with import fath")
    else:
        print("6) success!\n")


if __name__ == "__main__":
    main()

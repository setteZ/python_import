import importlib

try:
    from .. import fath as imp_fath
except Exception as e:
    print("error: fail to import from above dir")
    print(f"{e}")

if __name__ == "__main__":
    print("the main is running\n")
    
    print("## import_module from lower dir ##")
    try:
        bro_module = importlib.import_module("brother.bro")
        instance = bro_module.Brother()
        instance.print()
    except:
        print("error: fail to import_module brother.bro")
    else:
        print("success!")
    finally:
        print("")

    print("## import_module 1 from above dir ##")
    try:
        fath_module = importlib.import_module("fath", "..")
        instance = fath_module.Father()
        instance.print()
    except:
        print("error: fail 1 to import_module ..\\fath.py")
    else:
        print("success!")
    finally:
        print("")

    print("## import_module 2 from above dir ##")
    try:
        fath_module = importlib.import_module("..fath")
        instance = fath_module.Father()
        instance.print()
    except:
        print("error: fail 2 to import_module ..\\fath.py")
    else:
        print("success!")
    finally:
        print("")
    
    print("## import from upper dir ##")
    try:
        module = imp_fath.Father()
        module.print()
    except:
        print("error: fail with import fath")
    else:
        print("success!\n")

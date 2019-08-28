#!/usr/bin/python3


def demo_breakpoint():
    print("before_breakpoint")
    value = 0
    breakpoint()
    print(f"{value}")


if __name__ == "__main__":
    # export PYTHONBREAKPOINT=ipdb.set_trace
    demo_breakpoint()

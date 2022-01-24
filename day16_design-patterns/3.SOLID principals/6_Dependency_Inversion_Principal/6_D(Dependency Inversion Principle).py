"""
The dependency inversion principle (DIP) doesn't relate to Dependency Injection. So don't confuse yourself with it.

The dependency inversion principle (DIP) has two parts:

1. High-level modules should not depend on low-level modules. Instead, both should depend on abstractions (interfaces)
2. Abstractions should not depend on details. Details (like concrete implementations) should depend on abstractions.

                                       High level Module
                                        /            \
                                       /              \
                                      /                \
                                Low Level Module     Low Level Module
                                    /                     \
                                   /                       \                 =======> Bad Code
                                  /                         \
                            Lower Level Module          Lower level Module
                                /                             \
                               /                               \
                              /                                 \
                        The Lowest Level Module             The Lowest Level Module

Because in this case any change in other lower module will break our higher module.
DIP decouples high and low-level components and instead connects both to abstractions. High and low-level components
can still benefit from each other, but a change in one should not directly break the other.
The advantage of this part of DIP is that decoupled programs require less work to change. Webs of dependencies across
your program mean that a single change can affect many parts.
If you minimize dependencies, changes will be more localized and require less work to find all affected components.

"""

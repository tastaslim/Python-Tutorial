# Dependency inversion principle (DIP) #

The dependency inversion principle (DIP) doesn't relate to Dependency Injection(Rather Dependency Injection is one of
the way to implement the DIP). So don't confuse yourself with it.
The dependency inversion principle (DIP) has two parts:

**Program to interface not concrete implementation**

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

- Because in this case any change in other lower module will break our higher module.
  DIP decouples high and low-level components and instead connects both to abstractions. High and low-level components
  can still benefit from each other, but a change in one should not directly break the other.
  The advantage of this part of DIP is that decoupled programs require less work to change. Webs of dependencies across
  your program mean that a single change can affect many parts.
  If you minimize dependencies, changes will be more localized and require less work to find all affected components.

- Let's say we have a website, and we purchase few things from there which are stored in store menu card, and it
  redirects
  you to payments.
  Store ----- Stripe API // This is bad because now our store is directly related to Stripe API calls. What if in
  the future, you would like to change payment method to PayPal or PhonePe, you have to do tons of changes everywhere in
  the code of store logic as store is directly dependent on Stripe. This could be very hectic as we have to replace
  every stripe call with PayPal in store logic (because Store and Stripe are tightly coupled) and it violates Open
  Closed principal too.

# ----- Solution------

Instead of Store being directly attached to Stripe API, we should put a Payment processor abstraction in between them,
which will have functionalities related to payments. It will only contain function declarations not concrete
implementation. Any concrete implementation will implement all of its functionalities.
In this way if in the future, we want to replace Stripe with PayPal, we just need to pinpoint Payment processor to
PayPal.

                                                        Paypal
                                                       /
                                                      /
    Store  ----------- PaymentProcessor(Abstraction) ------------ PhonePe
                                                      \
                                                       \
                                                        Stripe

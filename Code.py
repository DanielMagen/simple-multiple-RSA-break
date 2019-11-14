from math import gcd


# based on
# https://algorithmsoup.wordpress.com/2019/01/15/breaking-an-unbreakable-code-part-1-the-hack/

def multiple_gcd(keys):
    """
    :param keys: a list of numbers
    (preferably such that each key shares at most 1 factor with the product of all other keys)
    :return: returns a list of the same length as the list of keys given, such that the list at location i would be
    the gcd(keys[i], product of all other keys)
    """
    if len(keys) == 1:
        return [keys[0]]
    if len(keys) == 2:
        gcd_of_elements = gcd(keys[0], keys[1])
        return [gcd_of_elements, gcd_of_elements]

    # else recurse on pairs of keys to get the answer
    # key_pairs_product[i] = keys[2i] * keys[2i + 1]
    key_pairs_product = []

    for i in range(0, len(keys) - 1, 2):
        key_pairs_product.append(keys[i] * keys[i + 1])
    if len(keys) % 2 == 1:
        key_pairs_product.append(keys[-1])

    results_for_pairs = multiple_gcd(key_pairs_product)
    # now results_for_pairs[i] = gcd(i'th key_pairs_product, product of all other key_pairs_product)
    # i.e results_for_pairs[i] = gcd(keys[2i] * keys[2i + 1], product of all other keys)
    # now there are 2 cases:
    # 1) results_for_pairs[i] divides either keys[2i] or keys[2i + 1]
    # 2) results_for_pairs[i] don't divide keys[2i] or keys[2i + 1]
    # both cases are good for our purposes

    final_results = []

    for i in range(0, len(keys), 2):
        final_results.append(gcd(keys[i], results_for_pairs[i // 2] * keys[i + 1]))
        final_results.append(gcd(keys[i + 1], results_for_pairs[i // 2] * keys[i]))

    if len(keys) % 2 == 1:
        # if the length of the list was odd, we simply added the last key to the list of pairs of keys.
        # then by the definition of the "results_for_pairs", it means that results_for_pairs[-1] will hold
        # the gcd(keys[-1], product of all other keys)
        # so simply append it to the list
        final_results.append(results_for_pairs[-1])

    return final_results


if __name__ == "__main__":
    ks = [10, 51, 6, 77]
    res = multiple_gcd(ks)
    print(res)

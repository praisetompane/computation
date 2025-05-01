def wrap(string, max_width):
    """Wrap text on specicifc max_width.

    Args:
        string (str): Text to wrap
        max_width (_type_): Max string length

    Returns:
        str: Wrapped string

    Remarks: This already exists in Python STL Text Processing Services
        implementation: https://github.com/python/cpython/blob/98e2c3af4794d6c6ebe47b20badbd31c542d944e/Lib/textwrap.py#L347
        usage:
        ```
            import textwrap

            def wrap(string, max_width):
                return "\n".join(textwrap.wrap(string, max_width))

        ```
    Performance Analysis:
        N = length of string
        W = max wdith

        Time = O(N/W)
        Space = O(N)
    """
    if len(string) < max_width:
        return string
    else:
        number_of_new_lines = len(string) // max_width
        string_parts = []
        last_index = 0
        for i in range(1, number_of_new_lines + 1):
            string_parts.append(string[last_index : max_width * i])
            last_index = max_width * i

        string_parts.append(string[max_width * number_of_new_lines :])
        return "\n".join(string_parts)

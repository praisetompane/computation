test("sort", () => {
    expect(sort([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5])
    expect(sort([4, 2, 3, 1, 5])).toEqual([1, 2, 3, 4, 5])
    expect(sort([])).toEqual([])
    expect(sort([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5])
});


test("bubble sort ascending", () => {
    expect(sort_explicit([5, 4, 3, 2, 1])).toEqual([1, 2, 3, 4, 5])
    expect(sort_explicit([4, 2, 3, 1, 5])).toEqual([1, 2, 3, 4, 5])
    expect(sort_explicit([])).toEqual([])
    expect(sort_explicit([1, 2, 3, 4, 5])).toEqual([1, 2, 3, 4, 5])
});
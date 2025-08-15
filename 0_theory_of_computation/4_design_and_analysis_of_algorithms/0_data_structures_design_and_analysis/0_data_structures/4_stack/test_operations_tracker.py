from use_cases.operations_tracker import OperationsTracker

text_processor = OperationsTracker("")


def test_all_operations_undoer():
    print("Praise typing his body of knowledge")
    print("My blank slate")
    assert text_processor.display() == ""
    assert text_processor.add_operations_result("I") == "I"
    assert text_processor.add_operations_result(" ") == "I "
    assert text_processor.add_operations_result("k") == "I k"
    assert text_processor.add_operations_result("m") == "I km"
    assert text_processor.undo() == "I k"
    assert text_processor.add_operations_result("n") == "I kn"
    assert text_processor.add_operations_result("o") == "I kno"
    assert text_processor.add_operations_result("w") == "I know"
    print("Try undo and redo")
    assert text_processor.undo() == "I kno"
    assert text_processor.redo() == "I know"
    assert text_processor.add_operations_result(" that") == "I know that"
    assert text_processor.undo() == "I know"

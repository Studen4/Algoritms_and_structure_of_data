"""Main module of program which show how works all lists"""
from node_single_linked import SingleLinkedList
from node_single_no_dub import SingleNoDub
from node_sorted_single import SortedSingle
from node_sorted_single_no_dub import SortedSingleNoDub
from node_double_linked import DoubleLinked
from node_double_no_dub import DoubleLinkedNoDub
from node_sorted_double import SortedDouble
from node_sorted_double_no_dub import SortedDoubleNoDub

my_list = SingleLinkedList()
my_list.append(1)
my_list.append(2)
print(my_list)

no_duplicates_list = SingleNoDub()
no_duplicates_list.append(1)
no_duplicates_list.append(2)
no_duplicates_list.append(2)
no_duplicates_list.append(3)
print(no_duplicates_list)

ordered_list = SortedSingle()
ordered_list.append(1)
ordered_list.append(3)
ordered_list.append(3)
ordered_list.append(2)
ordered_list.append(4)
print(ordered_list)

ordered_no_duplicates_list = SortedSingleNoDub()
ordered_no_duplicates_list.append(2)
ordered_no_duplicates_list.append(1)
ordered_no_duplicates_list.append(3)
ordered_no_duplicates_list.append(2)
ordered_no_duplicates_list.remove_duplicates()
print(ordered_no_duplicates_list)

doubly_list = DoubleLinked()
doubly_list.append(1)
doubly_list.append(2)
print(doubly_list)

doubly_no_duplicates_list = DoubleLinkedNoDub()
doubly_no_duplicates_list.append(1)
doubly_no_duplicates_list.append(2)
doubly_no_duplicates_list.append(2)
doubly_no_duplicates_list.append(3)
doubly_no_duplicates_list.remove_duplicates()
print(doubly_no_duplicates_list)

ordered_doubly_list = SortedDouble()
ordered_doubly_list.append(2)
ordered_doubly_list.append(1)
ordered_doubly_list.append(1)
ordered_doubly_list.append(3)
ordered_doubly_list.sort()
print(ordered_doubly_list)

ordered_doubly_no_duplicates_list = SortedDoubleNoDub()
ordered_doubly_no_duplicates_list.append(2)
ordered_doubly_no_duplicates_list.append(1)
ordered_doubly_no_duplicates_list.append(3)
ordered_doubly_no_duplicates_list.append(2)
ordered_doubly_no_duplicates_list.remove_duplicates()
ordered_doubly_no_duplicates_list.sort()
print(ordered_doubly_no_duplicates_list)

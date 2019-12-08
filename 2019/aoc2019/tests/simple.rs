use aoc2019;

#[test]
fn day1_part1() {
    assert_eq!(aoc2019::mass_to_fuel(12.), 2.);
    assert_eq!(aoc2019::mass_to_fuel(14.), 2.);
    assert_eq!(aoc2019::mass_to_fuel(1969.), 654.);
    assert_eq!(aoc2019::mass_to_fuel(100756.), 33583.)
    // part 1 correct answer: 3474920
}
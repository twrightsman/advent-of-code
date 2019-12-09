use aoc2019;

#[test]
fn day1_part1_simple() {
    assert_eq!(aoc2019::day1::mass_to_fuel(12), 2);
    assert_eq!(aoc2019::day1::mass_to_fuel(14), 2);
    assert_eq!(aoc2019::day1::mass_to_fuel(1969), 654);
    assert_eq!(aoc2019::day1::mass_to_fuel(100756), 33583)
}

#[test]
fn day1_part2_simple() {
    assert_eq!(aoc2019::day1::mass_to_total_fuel(14), 2);
    assert_eq!(aoc2019::day1::mass_to_total_fuel(1969), 966);
    assert_eq!(aoc2019::day1::mass_to_total_fuel(100756), 50346);
}
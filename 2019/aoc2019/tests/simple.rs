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

#[test]
fn day2_part1_simple() {
    // 1 + 1 = 2
    let mut memory = vec![1,0,0,0,99];
    aoc2019::day2::run_intcode_program(&mut memory);
    assert_eq!(memory, vec![2,0,0,0,99]);
    // 3 * 2 = 6
    let mut memory = vec![2,3,0,3,99];
    aoc2019::day2::run_intcode_program(&mut memory);
    assert_eq!(memory, vec![2,3,0,6,99]);
    // 99 * 99 = 9801
    let mut memory = vec![2,4,4,5,99,0];
    aoc2019::day2::run_intcode_program(&mut memory);
    assert_eq!(memory, vec![2,4,4,5,99,9801]);
    // more complex example
    let mut memory = vec![1,1,1,4,99,5,6,0,99];
    aoc2019::day2::run_intcode_program(&mut memory);
    assert_eq!(memory, vec![30,1,1,4,2,5,6,0,99]);
}
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

#[test]
fn day3_part1_simple() {
    assert_eq!(aoc2019::day3::closest_intersection("R8,U5,L5,D3", "U7,R6,D4,L4"), 6);
    assert_eq!(aoc2019::day3::closest_intersection("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"), 159);
    assert_eq!(aoc2019::day3::closest_intersection("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 135);
}

#[test]
fn day3_part2_simple() {
    assert_eq!(aoc2019::day3::fewest_steps("R8,U5,L5,D3", "U7,R6,D4,L4"), 30);
    assert_eq!(aoc2019::day3::fewest_steps("R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"), 610);
    assert_eq!(aoc2019::day3::fewest_steps("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"), 410);
}
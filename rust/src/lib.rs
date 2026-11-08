pub fn valid_trace(actions: &[&str]) -> bool {
    !actions.iter().any(|action| *action == "delete_without_approval")
}
#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn rejects_unapproved_delete() {
        assert!(!valid_trace(&["read", "delete_without_approval"]));
    }
}

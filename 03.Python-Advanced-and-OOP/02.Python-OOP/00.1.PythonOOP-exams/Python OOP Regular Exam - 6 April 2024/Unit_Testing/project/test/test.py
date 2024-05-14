from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):
    allowed_platforms = ['Instagram', 'YouTube', 'Twitter']

    def setUp(self):
        self.sm = SocialMedia(
            "TestName",
            "Twitter",
            100_000,
            "posting"
        )

    def test_correct_init(self):
        self.assertEqual("TestName", self.sm._username)
        self.assertEqual("Twitter", self.sm._platform)
        self.assertEqual(100_000, self.sm._followers)
        self.assertEqual("posting", self.sm._content_type)
        self.assertEqual([], self.sm._posts)

    def test__validate_and_set_platform_with_invalid_value_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sm._validate_and_set_platform("Facebook")

        self.assertEqual(f"Platform should be one of {self.allowed_platforms}", str(ve.exception))

    def test__validate_and_set_platform_with_valid_value_expect_success(self):
        self.sm._validate_and_set_platform("Instagram")

        self.assertEqual("Instagram", self.sm._platform)

    def test_followers_setter_with_invalid_number_raises(self):
        with self.assertRaises(ValueError) as ve:
            self.sm.followers = -1

        self.assertEqual("Followers cannot be negative.", str(ve.exception))

    def test_create_new_post_expect_success(self):
        new_post = {'content': "new_posting", 'likes': 0, 'comments': []}
        result = self.sm.create_post("new_posting")

        self.assertEqual(f"New {self.sm._content_type} post created by {self.sm._username} on {self.sm._platform}.",
                         result)
        self.assertEqual(self.sm._posts, [new_post])

    def test_like_post(self):
        self.sm._posts = [{'content': "new_posting", 'likes': 15, 'comments': []}]

        result = self.sm.like_post(3)
        self.assertEqual("Invalid post index.", result)

        result = self.sm.like_post(-1)
        self.assertEqual("Invalid post index.", result)

        result = self.sm.like_post(0)
        self.assertEqual("Post has reached the maximum number of likes.", result)

        self.sm._posts = [{'content': "new_posting", 'likes': 5, 'comments': []}]

        result = self.sm.like_post(0)
        self.assertEqual(f"Post liked by {self.sm._username}.", result)
        self.assertEqual(self.sm._posts[0]["likes"], 6)

    def test_comment_on_post_with_comment_length_less_than_10_characters(self):
        self.sm._posts = [{'content': "new_posting", 'likes': 15, 'comments': ["asd", "asdfghjjklo"]}]
        result = self.sm.comment_on_post(0, "asd")

        self.assertEqual("Comment should be more than 10 characters.", result)

    def test_comment_on_post_with_comment_length_more_than_10_characters(self):
        self.sm._posts = [{'content': "new_posting", 'likes': 15, 'comments': ["asd", "asdfghjjklo"]}]
        result = self.sm.comment_on_post(0, "asd12345678")

        self.assertEqual(f"Comment added by {self.sm._username} on the post.", result)


if __name__ == "__main__":
    main()

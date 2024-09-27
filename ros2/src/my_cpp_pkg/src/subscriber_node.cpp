#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"  // Include the message type

class MyNode : public rclcpp::Node
{
public:
    MyNode() : Node("cpp_test"), counter_(0)
    {
        RCLCPP_INFO(this->get_logger(), "Hello Cpp Node");

        // Create a timer to call the timerCallback function every 1 second
        /*timer_ = this->create_wall_timer(
            std::chrono::seconds(1), std::bind(&MyNode::timerCallback, this));  */

        // Create a subscriber for the "my_topic" topic
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "my_topic", 10, std::bind(&MyNode::topicCallback, this, std::placeholders::_1));
    }

private:
    /*void timerCallback()
    {
        counter_++;
        RCLCPP_INFO(this->get_logger(), "Pushpanjali %d", counter_);
    } */

    // Callback function for the subscriber
    void topicCallback(const std_msgs::msg::String::SharedPtr msg)
    {
        RCLCPP_INFO(this->get_logger(), "Received: '%s'", msg->data.c_str());
    }

    rclcpp::TimerBase::SharedPtr timer_;  // Timer to trigger the timerCallback
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr subscription_;  // Subscriber to the topic
    int counter_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<MyNode>();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}

#include <chrono>
#include <memory>
#include <string>

#include "rclcpp/rclcpp.hpp"
#include "diag_interfaces/msg/heartbeat.hpp"      
#include "diag_interfaces/msg/restart.hpp"


using namespace std::chrono_literals;

struct config_t{
    std::string appName;
    uint32_t appID;
};

enum appState_t{
    Start_up= 0x00,
    Running=0x01,
    Running_with_dtc=0x02,
    Running_after_dtc=0x03,
    Error=0x04
};


class IApplication : public rclcpp::Node{
public:
    IApplication(config_t config):Node(config.appName),state_(Start_up),count_(0){
        this->config_=config;
        hb_publisher_ = this->create_publisher<diag_interfaces::msg::Heartbeat>("HB", 10);
        hb_timer_ = this->create_wall_timer(
        1000ms, std::bind(&IApplication::hb_callback, this));
        this->reset_subscription_=this->create_subscription<diag_interfaces::msg::Restart>(
            "/Reset",10,std::bind(&IApplication::reset_callback,this,std::placeholders::_1));
    }
    void SetState(appState_t state){
        this->state_=state;
    }

private:
    config_t config_;
    appState_t state_;
    
    // Reset
    rclcpp::Subscription<diag_interfaces::msg::Restart>::SharedPtr reset_subscription_;
    void reset_callback(const diag_interfaces::msg::Restart msg) const{
        std::cout<<"reveived:"<<msg.app_id<<std::endl;
        if (msg.app_id==this->config_.appID){
            rclcpp::shutdown();
        }
    }
    //HB default variable
    uint64_t count_;
    rclcpp::TimerBase::SharedPtr hb_timer_;
    rclcpp::Publisher<diag_interfaces::msg::Heartbeat>::SharedPtr hb_publisher_;
    void hb_callback(){
        auto hb= diag_interfaces::msg::Heartbeat();                                   
        hb.app_id = this->config_.appID;  
        hb.timestamp=this->count_;
        hb.flags=this->state_;
        RCLCPP_INFO_STREAM(this->get_logger(), "Publishing : '" << hb.timestamp << "'");
        this->hb_publisher_->publish(hb);
        this->count_++;
    }
};
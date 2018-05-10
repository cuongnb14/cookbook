# install zsh
cd ~
echo "download and install zsh..."
sudo apt-get install -y zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# change theme and disable auto title
echo "change theme and disable auto title" 
sed -i 's/ZSH_THEME="robbyrussell"/ZSH_THEME="dpoggi"/' ~/.zshrc 
sed -i 's/\# DISABLE_AUTO_TITLE/DISABLE_AUTO_TITLE/' ~/.zshrc 


# auto jump
echo "install auto jump"
sudo apt-get install autojump
echo "source /usr/share/autojump/autojump.zsh" >> ~/.zshrc

# peco
echo "instsall peco"
wget https://github.com/peco/peco/releases/download/v0.5.1/peco_linux_amd64.tar.gz
tar -zxvf peco_linux_amd64.tar.gz && sudo cp peco_linux_amd64/peco /usr/local/bin/ && rm -r peco_linux_amd64 peco_linux_amd64.tar.gz

# zsh my config
echo "download zshrc_myconfig"
wget https://raw.githubusercontent.com/cuongnb14/cookbook/master/linux-config/.zshrc_myconfig
echo "source ~/.zshrc_myconfig" >> ~/.zshrc

# vim config
echo "config vim"
git clone --depth=1 https://github.com/amix/vimrc.git ~/.vim_runtime
sh ~/.vim_runtime/install_awesome_vimrc.sh

# Make ZSH the default shell
# chsh -s $(which zsh)
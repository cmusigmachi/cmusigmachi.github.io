module ApplicationHelper
  def random_image(opts = {})
    num_pics = Dir.entries(Rails.root.join('public')).size-2 #-2 for . and ..
    rand_pic = rand(num_pics) + 1
    
    image_tag("gallery/#{rand_pic}.jpg", opts.merge(:class => 'photo'){|key, oldval, newval| [oldval, newval].uniq.join(' ')})
  end  
end